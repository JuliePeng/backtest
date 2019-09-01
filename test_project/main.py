import flask

def get_version():
    return flask.__version__


if __name__ =='__main__':
    print(get_version())