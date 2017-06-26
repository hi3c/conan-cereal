from conans import ConanFile, CMake, tools
import os


class CerealConan(ConanFile):
    name = "cereal"
    version = "1.2.2"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        tools.download("https://github.com/USCiLab/cereal/archive/v1.2.2.tar.gz", "cereal.tar.gz")
        tools.unzip("cereal.tar.gz")

    def package(self):
        self.copy("*.hpp", dst="include", src="cereal-1.2.2/include")
        self.copy("*.h", dst="include", src="cereal-1.2.2/include")

    def package_info(self):
        self.cpp_info.libs = []
