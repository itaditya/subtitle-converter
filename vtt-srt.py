import subprocess,os,sys
class Converter():

    def __init__(self, location):
        self.location = location
        self.types = [".vtt",".srt"]
        self.mode = 0
        self.str_output = ""
        self.open_files()

    def open_files(self):
        type = self.types[self.mode]
        if(type == ".vtt"):
            call_fn = self.vtt_srt
        else:
            call_fn = self.srt_vtt
        for file_name in [f for f in os.listdir(self.location) if f.endswith(type)]:
            with open(file_name,"rb") as file:
                for line in file:
                    call_fn(line)
                output_type = self.types[1 - self.mode]
                output_file_name = file_name.replace(type,output_type)
                print("Converted '{}' to '{}'".format(file_name,output_file_name))
                self.save_file(output_file_name)
    def vtt_srt(self,line):
        flags = {"webvtt":True,"dots":True}
        if(flags["webvtt"] and "WEBVTT" in line):
            flags["webvtt"] = None
            line = line.replace("WEBVTT","")
        line = line.replace(".",",")
        line = line.replace("<v","")
        line = line.replace("</v>","")
        self.str_output += line

    def save_file(self,file_name):
        type = self.types[1 - self.mode]
        with open(file_name,"wb") as file:
            file.write(self.str_output)
            self.str_output = ""




def main():
    app = Converter(sys.argv[1])

if __name__ == '__main__':
    main()
