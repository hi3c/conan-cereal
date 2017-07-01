from conans import ConanFile, CMake, tools
import os


SHA1="a3c6ec47797f7f65403bdf5e9acadb18daa60586"

class CerealConan(ConanFile):
    name = "cereal"
    version = "a3c6ec4"
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
