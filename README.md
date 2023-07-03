[Prebuilt invoice model example](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/get-started-sdks-rest-api?view=form-recog-3.0.0&preserve-view=true&pivots=programming-language-python#prebuilt-model)


split pages:

```
sudo apt-get update
sudo apt-get install pdftk
pdftk <input file> burst output pages/<PREFIX>-%03d.pdf
```

## pipeline

* pdf_extractor
  * generate pickles from form recognizer
* postprocess
* fillin
* report 