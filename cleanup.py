import os
import shutil
import time
from PIL import Image
from PIL.ExifTags import TAGS
import datetime

# Comments: This organises up to modification date, except for pictures. It is a work in progress, because
# all a lot of specific file extensions get grouped into Other and have to ber manually moved.

desktop_path = input("Directory for cleanup: (eg: C:/Users/Asus/Desktop)   ")
now = datetime.date.today()

########################################################################################################################
# MODIFY THIS SECTION

# list of picture types
list_pictures = ["jpg", "png", "gif", "webp", "tiff", "psd", "raw", "bmp", "PNG"]
# list of documents types
list_documents = ["doc", "docx", "xls", "xlsx", "txt", "tex", "log", "dcx, aah, aag, aaf, aaa, aad,"
                                                                                  "bak", "pdf", "xml"]
# list of executables
list_executables = ["exe", "lnk", "url"]
# languages that will go to executables
list_languages = ["c", "cgi", "pl", "class", "cpp", "cs", "h", "java", "php", "py", "sh", "swift", "vb", "svg"]
# These will not be grouped in folders file
folder_exceptions = ["Folders", "Documents", "Executables", "Pictures", "Other"]

########################################################################################################################


def create_pictures_dir():
    """Handler for different picture formats and dates of creation"""
    obj_list = os.listdir(desktop_path)
    pictures_dir = os.path.join(desktop_path, "Pictures")
    if os.path.isdir(pictures_dir):
        pass

    else:
        os.mkdir(pictures_dir)
        no_year = os.path.join(pictures_dir, "NonIndexed")
        os.mkdir(no_year)

    for x in obj_list:
        if not os.path.isdir(x):
            if not x.find(".") == -1:
                try:
                    aux = x.split(".")
                    end = aux[1]
                except KeyError:
                    print(f"{x} is not OK")
                else:
                    if end in list_pictures:
                        old_path = os.path.join(desktop_path, x)
                        try:
                            metadata = Image.open(old_path).getexif()
                            if metadata != dict():

                                for tag_id in metadata:
                                    tag = TAGS.get(tag_id, tag_id)
                                    data = metadata.get(tag_id)

                                    if tag == "DateTime":
                                        list_data = str(data).split(":")
                                        year = list_data[0]
                                        year_path = os.path.join(pictures_dir, f"{year}")

                                        if not os.path.isdir(year_path):
                                            os.mkdir(year_path)
                                        new_path = os.path.join(pictures_dir, f"{year}" + "/" + x)
                                        shutil.move(src=old_path, dst=new_path)
                                        # create text LOG file:
                                        location = pictures_dir + "/" + "changes_pictures.txt"
                                        try:

                                            if not os.path.isfile(location):
                                                with open(file=location, mode="w") as f:
                                                    f.write(f"LOG: Moved {x} from {old_path} to {new_path}")

                                            else:
                                                with open(file=location, mode="a") as f:
                                                    f.write(f"\nLOG: Moved {x} from {old_path} to {new_path}")

                                        except FileNotFoundError:
                                            print("File not found. Check existence of subfolder")

                            else:
                                shutil.move(src=old_path, dst=pictures_dir + "/" + "NonIndexed" + "/" + x)
                                print(f"{x} has no metadata")

                        except KeyError:
                            raise ValueError


def create_executables_dir():
    """Handler for all types of executable objects"""
    obj_list = os.listdir(desktop_path)
    executables_path = desktop_path + "/" + "Executables"
    exe_executables_path = executables_path + "/" "exe"
    lnk_path = executables_path + "/" "lnk"
    py_path = executables_path + "/" + "Python"
    languages_dict = dict()

    if not os.path.isdir(executables_path):
        os.mkdir(executables_path)
    else:
        pass

    for x in obj_list:
        if not os.path.isdir(x):
            if not x.find(".") == -1:

                try:
                    aux = x.split(".")
                    end = aux[1]
                    old_path = desktop_path + "/" + x
                except KeyError:
                    print(f"{x} is not OK")
                else:
                    if end == "exe":
                        if not os.path.isdir(exe_executables_path):
                            os.mkdir(exe_executables_path)
                        shutil.move(src=old_path, dst=exe_executables_path + "/" + x)
                    if end == "lnk":
                        if not os.path.isdir(lnk_path):
                            os.mkdir(lnk_path)
                        shutil.move(src=old_path, dst=lnk_path + "/" + x)
                    # List of some programming languages:
                    if end in list_languages:
                        languages_dict[f"{end}"] = executables_path + "/" f"{end}"
                        if not os.path.isdir(languages_dict[f"{end}"]):
                            os.mkdir(languages_dict[f"{end}"])
                        shutil.move(src=old_path, dst=languages_dict[f"{end}"] + "/" + x)


def create_documents_dir():
    """Handles documents with different file types and
    dates of creation"""
    obj_list = os.listdir(desktop_path)
    documents_dir = desktop_path + "/" + "Documents"
    no_year = documents_dir + "/" + "NonIndexed"

    if os.path.isdir(documents_dir):
        pass
    else:
        os.mkdir(documents_dir)
        os.mkdir(no_year)

    for x in obj_list:
        if not os.path.isdir(x):
            if not x.find(".") == -1:
                try:
                    aux = x.split(".")
                    end = aux[1]
                except KeyError:
                    print(f"{x} is not OK")
                else:
                    if end in list_documents:
                        # creating directories for present file
                        old_path = desktop_path + "/" + x
                        directory_path = documents_dir + "/" + end

                        if not os.path.isdir(directory_path):
                            os.mkdir(directory_path)

                        try:
                            date = os.path.getmtime(old_path)
                            modification_date = time.ctime(date)
                            mod_date_final = time.strptime(modification_date).tm_year
                            year_path = directory_path + "/" + f"{mod_date_final}"

                            if not os.path.isdir(year_path):
                                os.mkdir(year_path)
                            location = documents_dir + "/" + "changes_documents.txt"
                            shutil.move(src=old_path, dst=year_path + "/" + x)

                            try:
                                if not os.path.isfile(location):
                                    with open(file=location, mode="w") as f:
                                        f.write(f"LOG: Moved {x} from {old_path} to {year_path} at {now}")

                                else:
                                     with open(file=location, mode="a") as f:
                                        f.write(f"\nLOG: Moved {x} from {old_path} to {year_path} at {now}")

                            except FileNotFoundError:
                                print("File not found. Check existence of subfolder")

                        except KeyError:
                            print(f"{x} has no modification date")


def other():
    """Handles all other unknown filem formats and bundles folders into
    Folders file"""
    obj_list = os.listdir(desktop_path)
    other_path = desktop_path + "/" + "Other"
    folders = desktop_path + "/" + "Folders"
    unknown_formats = []

    for x in obj_list:
        try:
            ext = x.split(".")[1]
        except IndexError or shutil.Error:
            print(f"{x} is a folder")
            if not os.path.isdir(folders):
                os.mkdir(folders)
            if x not in folder_exceptions:
                try:
                    shutil.move(src=desktop_path + "/" + x, dst=folders)
                except shutil.Error:
                    print(f"Folder {x} already exists in Folders")
                finally:
                    pass
        else:
            if not os.path.isdir(other_path):
                os.mkdir(other_path)

            try:
                if not os.path.isdir(x):
                    shutil.move(src=desktop_path + "/" + x, dst=other_path)
                    try:
                        text_loc = other_path + "/" + "change_other.txt"
                        if os.path.isfile(other_path):
                            with open(file=text_loc, mode="w") as f:
                                f.write(f"LOG: Moved {x} from {desktop_path} to {other_path} at {now}")

                        else:
                            with open(file=text_loc, mode="a") as f:
                                f.write(f"\nLOG: Moved {x} from {desktop_path} to {other_path} at {now}")

                    except PermissionError:
                        print(f"File {x} has weird permissions")

                    finally:
                        pass

            except PermissionError:
                print(f"Folder {x} has weird permissions")

    print(f"Unkown formats: {unknown_formats}")


if __name__ == '__main__':
    create_pictures_dir()
    create_executables_dir()
    create_documents_dir()
    other()




