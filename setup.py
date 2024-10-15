from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="f5tts",
    version="0.0.1",
    description="F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching",
    url="https://github.com/aluebs/F5-TTS",
    packages=find_packages(),  # Discover packages under the root
    include_package_data=True,  # Ensure package_data is included
    install_requires=install_requires,
    package_data={
        "": ["data/**/*"],  # Recursively include all files in data/
    },
    zip_safe=False,  # Prevent zipping for easier access
)
