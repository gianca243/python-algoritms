# www.google.com
# www.myservice.com/12341243
import hashlib
url_store = {
    "id": "",
    "12331424": "www.google.com"
}
MY_URL = "www.mydomain.com/"
def short_url(url: str) -> str:
    h = hashlib.new('sha256')
    h.update(url.encode())
    new_id = h.hexdigest().split()[0]
    new_id = new_id[:7]
    new_url = MY_URL + new_id
    url_store.update({
        f"{new_id}": url
    })
    return new_url

def return_previous_url(short_url: str) -> str:
    id = short_url.split("/")[1]
    if id in url_store.keys():
        return {"status": 200, "url": url_store.get("id")}
    else:
        return {"status": 401, "message": "sorry, this is not a valid id"}


if __name__ == "__main__":
    short_result = short_url("www.google.com")
    print(f"short url is {short_result}")
    previos_result = return_previous_url(short_result)
    print(f"input was {previos_result}")




