[Prebuilt invoice model example](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/get-started-sdks-rest-api?view=form-recog-3.0.0&preserve-view=true&pivots=programming-language-python#prebuilt-model)


split pages:

```
sudo apt-get update
sudo apt-get install pdftk

```
pdftk data/CFIA_ACIA\ -\ #19462390\ -\ v1\ -\ NFLD.PDF burst output pages/NFLD-%03d.pdf
pdftk data/"CFIA_ACIA - #19462394 - v1 - Quebec.PDF" burst output pages/Quebec-%03d.pdf
pdftk "/workspaces/louis-invoices/data/CFIA_ACIA - #19462393 - v1 - PEI.PDF" burst output pages/PEI-%03d.pdf
pdftk "/workspaces/louis-invoices/data/CFIA_ACIA - #19462397 - v1 - New Brunswick.PDF" burst output pages/New Brunswick-%03d.pdf
pdftk "/workspaces/louis-invoices/data/CFIA_ACIA - #19462397 - v1 - New Brunswick.PDF" burst output pages/NewBrunswick-%03d.pdf
pdftk "data/CFIA_ACIA-#19462387-v1-NS.PDF" burst output pages/NS-%03d.pdf
```