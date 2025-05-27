import requests
import json

def get_title_data(sessionTicket):
    try:
        r = requests.post(
            url="https://63FDD.playfabapi.com/Client/GetTitleData",
            headers={
                "Content-Type": "application/json",
                "X-Authorization": sessionTicket
            },
            json={}s
        )
        if r.status_code == 200:
            return r.json()
        else:
            return r.status_code
    except Exception as e:
        print(f"Error : {e}")
        return None
def main():
    print("Input your session ticket!")
    sesh = input(">> ")
    r_json = get_title_data(sesh)
    if r_json == 401:
        print("Error, try again.")
    if r_json == None:
        print("Error in get request.")
    del r_json['code']
    del r_json['status']
    title_data = r_json['data']['Data']
    del r_json['data']
    r_json['TitleData'] = title_data

    try:
        with open("title_data.json", 'w') as file:
            file.write(json.dumps(r_json, indent=4))
    except Exception as e:
        print(f"Error : {e}")

    print("Title Data saved to title_data.json.")

if __name__ == "__main__":
    main()