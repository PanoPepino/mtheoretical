from setuptools import setup, find_packages

setup(
    name= "beanim",
    version= "1.0",
    packages= find_packages(where= "src"),
    package_dir= {"": "src"},
    package_data={
        "beanim": ["figures/*.png", "figures/*.jpg", "figures/*.gif", "figures/*.svg"], #This is to also include specific files.
        #It requires some tweaks in the MANIFEST file also. 
    },
    include_package_data= True,
    install_requires= [
        "numpy>=1.21.0",
        "manim>=0.17"
    ],
)
