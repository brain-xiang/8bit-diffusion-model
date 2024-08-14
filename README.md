# 8bit-diffusion-model


![DEMO](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXIyamkzanFyOG9md2FhbXgwenB3bWIycHIyZGZ4ZmgzYnBlZjBpaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8PtlTNQEBCtP12dMrN/giphy.gif)

A lightweight foundational diffusion model (1.4M params) that generates 8-bit game sprites. Built from scratch with a custom architecture, trained on just **894 images**. This repository features the architecture, data, and source code for both the training and inference.

This repository is mostly meant for **experimental and educational purposes**. It does not include any production ready code or functional use cases.

## Features
* 894-image dataset of 8bit video game assets
* Implementation Unet architecture in TensorFlow
* Hyperparameter Tuning using keras_tuner
* Custom training and test loops
* DDPM & DDIM sampling / inference
* Saving and loading options
* Visualization (png, gifs)

## Data vs. Generations
| Data samples | Generated Samples |
|:---------------------:|:----------------------:|
| ![Data samples](https://github.com/brain-xiang/8bit-diffusion-model/blob/main/images/data_samples.png) | ![Generated Samples](https://github.com/brain-xiang/8bit-diffusion-model/blob/main/images/generated_samples.png) |


## Architecture
![Architecture](https://github.com/brain-xiang/8bit-diffusion-model/blob/main/Architecture.jpg)

## Setup
All of the relevant training and inference code is contained within a self sustained jupyter notebook (**notebooks/main_notebook.ipynb**). The notebook is organized with headings and descriptions on how to train a new model or load the pre-trained model and run inference. So all you need to do is:
1. clone the repository 
2. Download dependencies and libraries required from "requirements.txt"
3. Run notebooks/main_notebook.ipynb

Repository structure
* Data - features the 849-image dataset used to train the model
* Generations - features pre-generated samples using the model
* images - some image extracts
* notebooks - features the main self-contained notebook which contains the implementation
* util - some utility .py scripts to download and visualize samples
* weights - the weights and configs of pre-trained models
* architecture.jpg - the model architecture (high def image)

Note: The model was trained using the directml plugin of tensorflow to leverage AMD GPUs. This plugin only works with tensorflow–cpu==2.10. More info here: https://learn.microsoft.com/en-us/windows/ai/directml/gpu-tensorflow-plugin

## Acknowledgments
- Sprites by ElvGames, [FrootsnVeggies](https://zrghr.itch.io/froots-and-veggies-culinary-pixels) and  [kyrise](https://kyrise.itch.io/)
- Diffusion model is based on [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) and [Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502)

## Contact
Created by [Brain Xiang](https://x.com/brain_xiang) - feel free to contact me!
