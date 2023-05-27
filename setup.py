from setuptools import setup, find_packages

setup(
    name='books-shared',
    version='0.2.1',
    author='Oleksandr Zhukov',
    description='Shared modules for book store project',
    url='https://github.com/Alexzhukoff86/book-shared',
    keywords='development, setup, setuptools, wheel',
    python_requires='==3.8',
    packages=find_packages(),
    install_requires=[
        "grpcio_tools == 1.33.2",
        "grpcio-reflection == 1.33.2",
        "python-dotenv == 1.0.0",
        "Flask-SQLAlchemy == 3.0.3",
        "Faker==18.9.0"
    ]
)