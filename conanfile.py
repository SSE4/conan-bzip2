#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools


class Bzip2Conan(ConanFile):
    name = "bzip2"
    version = "1.0.6"    
    url = "https://github.com/conan-community/conan-bzip2"
    homepage = "http://www.bzip.org"
    author = "Conan Community"
    license = "bzip2-1.0.6"
    description = "bzip2 is a free and open-source file compression program that uses the Burrows–Wheeler algorithm."
    topics = ("conan", "bzip2", "data-compressor", "file-compression")
    settings = "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    exports = "LICENSE"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"
    _source_subfolder = "source_subfolder"
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        folder_name = "%s-%s" % (self.name, self.version)
        zip_name = "%s.tar.gz" % folder_name
        sha256 = "a2848f34fcd5d6cf47def00461fcb528a0484d8edef8208d6d2e2909dc61d9cd"
        url = "https://bintray.com/conan/Sources"
        tools.get(url="%s/download_file?file_path=%s" % (url, zip_name), sha256=sha256, filename=zip_name)
        os.rename(folder_name, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        tools.replace_in_file(os.path.join(self._source_subfolder, "bzip2.c"), r"<sys\stat.h>", "<sys/stat.h>")
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ['bz2']
