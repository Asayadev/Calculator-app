name: Build Android APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Build with Buildozer
      uses: ArtemShedov/buildozer-action@v1.2.1
      with:
        command: buildozer -v android debug
        repository_root: .

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: Calculator-APK
        path: bin/*.apk
