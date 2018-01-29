from cx_Freeze import setup, Executable

include_files = [ 'app/templates/',
                  'app/static/',]

# Note: without 'jinja2.ext' in this list, we won't get the templates working. 

include = [ 'jinja2', 'jinja2.ext',]
flaskapp = Executable(script="run.py",
                      base="Win32GUI",
                       targetName="mando_esp8266.exe",
                       copyDependentFiles=True,
                       icon="rocket.ico"

                  )
setup(
    name="mando esp8266",
    version="1.0",
    author="jorge garcia",
    description="mando esp8266",
    options={
        'build_exe': {
            'include_files': include_files,
            'includes': include,
            'build_exe': "build"
        }
    },
    executables=[flaskapp]
)