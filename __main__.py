class myClient:
    import socket  # Import socket module

    while True:
        subject = input("Please enter the subject (C#, c++, CMake, Linux, Compilers)")
        subject.lower()
        question = input("what is your question?")

        if (question != '' and subject != ''):
            qt = question.encode()
            st = subject.encode()
            s = socket.socket()  # Create a socket object
            host = socket.gethostname()  # Get local machine name
            port = 60000  # Reserve a port for your service.
            s.connect((host,port))
            s.send("Subject ".encode()+ st + " ".encode() + "Question ".encode() + " ".encode() + qt)
            s.close()
            print('Question Send!\n')