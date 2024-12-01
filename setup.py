from setuptools import setup

setup(
    name="streamdiffusion",
    version="0.1.0",
    description="StreamDiffusion project dependencies",
    install_requires=[
        "torch==2.1.0",
        "torchvision==0.16.0",
        "xformers",
        "huggingface-hub==0.23.2",
        "diffusers==0.30.0",
        "protobuf==5.27.2"
    ],
    python_requires=">=3.10",
)
