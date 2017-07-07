from conans import ConanFile, CMake, tools
import os


SHA1="a9c149424b217deea63e2b023b3c48bd1e9f42bc"

class CerealConan(ConanFile):
    name = "cereal"
    version = "a9c1494"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    generators = "cmake"
    exports_sources = "src/*"
    requires = "boost/1.64.0_1@hi3c/experimental"

    def source(self):
        tools.download("https://github.com/hi3c/cereal/archive/{}.zip".format(SHA1), "cereal.zip")
        tools.unzip("cereal.zip")
        os.remove("cereal.zip")

    def package(self):
        self.copy("*.hpp", dst="include", src="cereal-{}/include".format(SHA1))
        self.copy("*.h", dst="include", src="cereal-{}/include".format(SHA1))

    def package_info(self):
        self.cpp_info.libs = []
