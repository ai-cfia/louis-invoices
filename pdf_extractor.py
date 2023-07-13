# import libraries
import dotenv
dotenv.load_dotenv()

import pickle
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# set `<your-endpoint>` and `<your-key>` variables with the values from the Azure portal
endpoint = os.environ.get('AZURE_FORMRECOGNIZER_ENDPOINT')
key = os.environ.get('AZURE_FORMRECOGNIZER_KEY')

def format_bounding_region(bounding_regions):
    if not bounding_regions:
        return "N/A"
    return ", ".join("Page #{}: {}".format(region.page_number, format_polygon(region.polygon)) for region in bounding_regions)

def format_polygon(polygon):
    if not polygon:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in polygon])


def analyze_invoice(fileHandle):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_analysis_client.begin_analyze_document(
            "prebuilt-invoice", document=fileHandle)
    invoices = poller.result()
    return invoices



if __name__ == "__main__":
    dirname, filename = os.path.split(os.path.abspath(__file__))
    source_dir = "data/pages/"
    filenames = os.listdir(source_dir)
    for filename in filenames:
        if not filename.endswith('pdf'):
            continue
        fullpath = os.path.join(dirname, source_dir, filename)
        print(f'Processing {fullpath}')
        with open(fullpath, "rb") as f:
            pickle_filename = fullpath + '.pickle'
            if os.path.isfile(pickle_filename):
                print(f"{pickle_filename} already exists, skipping")
                continue
            invoices = analyze_invoice(f)
            with open(pickle_filename, "wb") as picklefile:
                pickle.dump(invoices, picklefile)
