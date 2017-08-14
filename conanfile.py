from conans import ConanFile, CMake, tools
import os


SHA1="8f472911c26b8677f45de726d721e2d4774a7d86"

class CerealConan(ConanFile):
    name = "cereal"
    version = "8f47291"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    generators = "cmake"
    exports_sources = "src/*"

    def source(self):
        tools.download("https://github.com/hi3c/cereal/archive/{}.zip".format(SHA1), "cereal.zip")
        tools.unzip("cereal.zip")
        os.remove("cereal.zip")

    def package(self):
        self.copy("*.hpp", dst="include", src="cereal-{}/include".format(SHA1))
        self.copy("*.h", dst="include", src="cereal-{}/include".format(SHA1))

    def package_info(self):
        self.cpp_info.libs = []
