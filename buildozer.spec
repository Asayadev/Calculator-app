[app]

# (str) Title of your application
title = Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory names to not include
source.exclude_dirs = tests, bin, buildozer, .github

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.2.1

# (str) Supported orientation (one of: landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (bool) Wipe build directory (clean build)
# wipe_build = False

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (int) Android API level (SDK version)
android.api = 33

# (int) Android minimum API level
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 23b

# (str) Android build tools version
android.build_tools = 30.0.3

# (bool) Enable Android debug mode
android.debug = True

# (list) Android permissions
android.permissions = INTERNET
