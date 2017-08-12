from setuptools import setup


setup(
    name='sketchapp',
    version='0.0.1',
    packages=['sketchapp'],
    options={
        'app': {
            'formal_name': 'Sketch App',
            'bundle': 'org.pybee.elias'
        },
    }
)
