[![Download](https://api.bintray.com/packages/conan-community/conan/bzip2%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/bzip2%3Aconan/_latestVersion)
[![Build status](https://ci.appveyor.com/api/projects/status/github/ConanCIintegration/conan-bzip2?svg=true)](https://ci.appveyor.com/project/ConanCIintegration/conan-bzip2)
[![Build Status](https://travis-ci.org/conan-community/conan-bzip2.svg)](https://travis-ci.org/conan-community/conan-bzip2)
# Conan BZip2

 ![logo](logo.png)

Conan package for BZip2 library. http://www.bzip.org/

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/bzip2%3Aconan).

## Basic setup

    $ conan install bzip2/1.0.6@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    bzip2/1.0.6@conan/stable

    [options]
    bzip2:shared=true # false
    bzip2:fPIC=true # false (only available for Linux and Macos)

    [generators]
    cmake

## Issues

If you wish to report an issue for Conan Community related to this package or any other, please do so here:

[Conan Community Issues](https://github.com/conan-community/community/issues)

## Wish List

If you wish to make a request for Conan Community creating a new package, please do so here:

[Conan Wish List](https://github.com/conan-io/wishlist)


## License

[MIT](LICENSE)