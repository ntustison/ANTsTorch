import torchvision
import os

def get_pretrained_network(file_id=None,
                           target_file_name=None,
                           antstorch_cache_directory=None):

    """
    Download pretrained network/weights.

    Arguments
    ---------

    file_id string
        One of the permitted file ids or pass "show" to list all
        valid possibilities. Note that most require internet access
        to download.

    target_file_name string
       Optional target filename.

    antstorch_cache_directory string
       Optional target output.  If not specified these data will be downloaded
       to the subdirectory ~/.antstorch/.

    Returns
    -------
    A filename string

    Example
    -------
    >>> model_file = get_pretrained_network('not_yet')
    """

    def switch_networks(argument):
        switcher = {
            "chexnet_repro_pytorch": "https://figshare.com/ndownloader/files/42411897",
            "mriModalityClassification": "https://figshare.com/ndownloader/files/41692998"
        }
        return(switcher.get(argument, "Invalid argument."))

    if file_id == None:
        raise ValueError("Missing file id.")

    valid_list = ("chexnet_repro_pytorch",
                  "mriModalityClassification",
                  "show")

    if not file_id in valid_list:
        raise ValueError("No data with the id you passed - try \"show\" to get list of valid ids.")

    if file_id == "show":
       return(valid_list)

    url = switch_networks(file_id)

    if target_file_name is None:
        target_file_name = file_id + ".h5"

    if antstorch_cache_directory is None:
        antstorch_cache_directory = os.path.join(os.path.expanduser('~'), '.antstorch/')
    target_file_name_path = os.path.join(antstorch_cache_directory, target_file_name)

    if not os.path.exists(target_file_name_path):
        torchvision.datasets.utils.download_url(url,
                                                antstorch_cache_directory,
                                                target_file_name)

    return(target_file_name_path)
