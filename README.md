
# iPhone Media Share to PC API

This repository contains the implementation of an API designed to facilitate the sharing of media files from an iPhone to a PC. It leverages a simple yet efficient approach to transfer files securely and swiftly between your iPhone and PC using a web-based interface.

## Features

- **Easy Media Transfer**: Simplifies the process of transferring files from your iPhone to your PC.
- **Secure**: Implements basic security measures to ensure that media transfers are secure.
- **Cross-Platform Compatibility**: Works across different operating systems on the PC, including Windows, macOS, and Linux.

## How It Works

1. **Connection Setup**: Users initiate the connection by accessing the web interface hosted on the PC from their iPhone's browser.
2. **Media Selection**: Users select the media files they wish to transfer from their iPhone.
3. **Transfer Initiation**: After selection, the transfer process begins, securely uploading the files to the PC.
4. **Completion**: Once the transfer is complete, users receive a confirmation, and the files are accessible on the PC.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Install the necessary dependencies using `pip install -r requirements.txt`.
3. **Start the Server**: Launch the server on your PC using `python manage.py runserver`.
4. **Access from iPhone**: Open your iPhone's browser and navigate to the IP address displayed in the terminal.

## Configuring for iPhone to PC File Transfer
1. **Get Your IP Address**: On Ubuntu, open the terminal and run the following command to get your IP address:
	```bash
	ifconfig -a
	```
	Look for the `inet` address under your active network interface (e.g., `eth0` or `wlan0`). This is your IP address.


2. **Update JavaScript Code**: In the `media_form.html` file, update the following line of JavaScript to use your IP address instead of `127.0.0.1`:
	```js
	xhr.open('POST', `http://your_ip_address:8000/uploader/`, true);
	```
3. **Running the Application on Your PC**:  To run the application on your PC, use the 		  following command:
	 ``` 
	 python manage.py runserver 0.0.0.0:8000
	```
  
4. **Access the Upload Form from iPhone**: On your iPhone's Safari browser, navigate to:
	```js
	http://your_ip_address:8000
	```
	 This will allow you to transfer files from your iPhone to your PC.

## Dependencies

- Django: For the backend server and API.
- Bootstrap: For the frontend design.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

