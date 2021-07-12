import datetime

class FileHandler:
    os = 0
    def __init__(self,os):
        self.os = os
        print("Webserver initiated")

    def get_filename(
        self,
        start,
        end,
        region = "DE-50HZ",
        data_type = "forecast", #"historical",#live
        forecast_type = "statistical",#"deep_learning","entsoe"
        ):
        # Declaration:
        # this function is used as a data handler for the storgae system. 
        # It will ask for the data and if it is not existing pull it.

        # file structuring: 
        #                    regions(5 possibilities)      #region
        #                  /                \
        #               forecast            historical     #data_type
        #           /     |        \
        #  statistical   entsoe deep_learning              #forecast_type
        filename    = start.strftime('%Y-%d-%m') +region+ '.csv'
        directory   = self.os.path.abspath("rsc")
        try:
            self.os.stat(directory)
        except:
            self.os.mkdir(directory)       
        directory = self.os.path.join(directory,region)
        try:
            self.os.stat(directory)
        except:
            self.os.mkdir(directory)
        directory = self.os.path.join(directory,data_type)
        try:
            self.os.stat(directory)
        except:
            self.os.mkdir(directory)
        if data_type == "forecast":
            directory = self.os.path.join(directory,forecast_type)
            try:
                self.os.stat(directory)
            except: 
                self.os.mkdir(directory)
        filename = self.os.path.join(directory,filename)
        filename = self.os.path.abspath(filename)
        return filename

    def test_file_exists(self, filepath):
        if (self.os.path.exists(filepath)):
            return True
        else:
            return False