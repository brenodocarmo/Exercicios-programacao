def two_fer(name=None):
    if name is None:
        return 'One for you, one for me.'
    return 'One for {}, one for me.'.format(name)



if __name__ == "__main__":
    two_fer('breno')
    two_fer()
    

