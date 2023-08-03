# piazza-ping
# About
Piazza Ping is a simple utility tool desgined to help students stay updated about new unread posts in their Piazza class forum. It checks for new posts and sends instant notifications to users on their desktop.
Piazza's internal API is currently private, however a unofficial client for the API was able to be used instead: https://github.com/hfaran/piazza-api
# Installation
```
git clone https://github.com/sp1603/piazza-ping
cd piazza-ping
pip install -r requirements.txt
```
Once installed you will need to configure a credentials.json file (see Configuration) and then run the following command.
```
python piazza_ping.py
```

# Configuration

You will need to create a credentials.json file as piazza requires login information as well as class codes.
Here is a sample layout of what the  credentials.json file should look like.

To find the network id of the piazza class, a piazza url is of the following format: https://piazza.com/class/NETWORKID
It will have a combination of letters and numbers.

Currently, there is only support for 2 classes.
```
{
    "email": "georgepburdell@gatech.edu",
    "password": "georgepburdell",
    "network_ids": [
        "georgepburdell123",
        "georgepburdell456"
    ],
    "class_names": [
        "GEORGEPBURDELL101",
        "GEORGEPBURDELL102"
    ]
    
    
}
```

# Contributions
Contributions are welcome.

1. Fork the repository.
2. Create a new branch: ```git checkout -b feature/your-feature-name```.
3. Make your changes and commit them: ```git commit -m "Add your feature"```.
4. Push the changes to your branch: ```git push origin feature/your-feature-name```.
5. Open a pull request, explaining the changes you made.
