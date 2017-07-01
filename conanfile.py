from conans import ConanFile, CMake, tools
import os


SHA1="67f742f3607bd3c65eb4911dc0dee659703d2275"

class CerealConan(ConanFile):
    name = "cereal"
    version = "67f742f"
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
