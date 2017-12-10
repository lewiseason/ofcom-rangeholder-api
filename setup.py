from distutils.core import setup

setup(name='ofcom-rangeholder-api',
      version='0.1.0',
      description='HTTP JSON API for Ofcom Rangeholder lookups',
      author='Lewis Eason',
      author_email='me@lewiseason.co.uk',
      url='https://github.com/lewiseason/ofcom-rangeholder-api',
      packages=['ofcom_rangeholder_api'],
      install_requires=[
        'Flask==0.12.2',
        'flask-cors',
        'phonenumbers==8.8',
        'docopt==0.6.2'
      ],
      entry_points={
        'console_scripts': [
            'ofcom-rangeholder-api=ofcom_rangeholder_api.cli:main'
        ]
      })
