import requests


class TestFileUploadDownload:
    BASE_URL = "http://localhost:8080"
    File_1 = "D:/Postman_ResponseValidations.pdf"
    file_2 = "D:/Scripts+in+Postman.txt"

    def test_singleFile(self):
        with open(self.File_1, "rb") as f:
            files = {"file": f}
            res = requests.post(f"{self.BASE_URL}/uploadFile", files=files)
        assert res.status_code == 200, "Upload failed"
        data = res.json()
        data['fileName'] = "Postman_ResponseValidations.pdf", "Wrong Upload"
        print(data)

    def test_MultipleFile(self):
        with open(self.File_1, "rb") as f1, open(self.file_2, "rb") as f2:
            files = [("files", f1), ("files", f2)]
            res = requests.post(f"{self.BASE_URL}/uploadMultipleFiles", files=files)
        assert res.status_code == 200, "Upload failed"
        data = res.json()
        print(data)

    def test_download_file(self):
        filename = "Postman_ResponseValidations.pdf"
        res = requests.get(f"{self.BASE_URL}/downloadFile/{filename}")
        assert res.status_code == 200, "Wrong Status Code"
        output_path = f"downloaded_{filename}"
        with open(output_path, "wb") as f:
            f.write(res.content)
