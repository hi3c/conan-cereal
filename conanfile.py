from conans import ConanFile, CMake, tools
import os


SHA1="7a58c34e87c791f4b8a36f9b4933f1bc426db7ff"

class CerealConan(ConanFile):
    name = "cereal"
    version = "7a58c34"
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
