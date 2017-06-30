from conans import ConanFile, CMake, tools
import os


class CerealConan(ConanFile):
    name = "cereal"
    version = "2.6.2"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    generators = "cmake"
    exports_sources = "src/*"

    def source(self):
        pass

    def package(self):
        self.copy("*.hpp", dst="include", src="src/include")
        self.copy("*.h", dst="include", src="src/include")

    def package_info(self):
        self.cpp_info.libs = []
