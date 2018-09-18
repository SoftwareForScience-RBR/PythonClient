class myServer:
    import socket  # Import socket module

    while True:
        question = input("what is your question?")

        if (question != ''):
            print('sendin Message!')
            qt = question.encode()
            s = socket.socket()  # Create a socket object
            host = socket.gethostname()  # Get local machine name
            port = 60000  # Reserve a port for your service.
            s.connect((host,port))
            s.send(qt)
            s.close()



