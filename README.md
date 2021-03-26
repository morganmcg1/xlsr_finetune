# XLSR Finetune
> A bunch of handy functions to make fine-tuning the XLSR-Wav2Vec2 speech recognition model much easier

## Clean XLSR Code
This contains clean simple code to do much of the setup, data exploration, data processing, training, logging and data versioning to enable easier fine-tuning of XLSR-Wav2Vec2. Create during the [Hugging Face XLSR community effort](https://discuss.huggingface.co/t/open-to-the-community-xlsr-wav2vec2-fine-tuning-week-for-low-resource-languages/4467).

### Thanks
Much of the code in this project is taken from Patrick Von Platen's brilliant Hugging Face [blog post here](https://huggingface.co/blog/fine-tune-xlsr-wav2vec2)

## Getting Started
See the [Demo Training notebook](https://github.com/morganmcg1/xlsr_finetune/blob/master/notebooks/_train_demo.ipynb) at `xlsr_finetune/notebooks/_train_demo.ipynb` for an end-to-end example of data processing, model training, metrics logging and data and model versioning

## Install

```
git clone https://github.com/morganmcg1/xlsr_finetune.git

cd xlsr_finetune

pip install -e .

```

or you can run the below directly from a notebook

```
pip install git+https://github.com/morganmcg1/xlsr_finetune.git
```

## Contributing

To contribute, make sure you have the latest version of nbdev installed and read the `CONTRIBUTING.md` file
