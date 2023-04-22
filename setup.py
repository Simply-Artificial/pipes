from setuptools import setup

setup(
    name='sa-pipes',
    version='{{VERSION_PLACEHOLDER}}',
    description="Simply Artificial's transformer pipelines",
    url='https://github.com/Simply-Artificial/pipes',
    author='ItsMeAlfie0',
    author_email='simply-artificial@itsmealfie0.com',
    license='MIT',
    packages=[
        'pipes'
        'pipes.SADispatch'
    ],
    install_requires=open('requirements.txt').read().splitlines(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
