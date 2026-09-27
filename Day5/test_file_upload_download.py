import requests

class TestFileUploadDownload:
    BASE_URL = "http://localhost:8080"
    File1 = "./Test1"
    File2 = "./Test2"

    def test_upload_single_file(self):
        with open(self.File1, "rb") as file:
            files = {"file": file}
            res = requests.post(f"{self.BASE_URL}/uploadFile", files=files)
        assert res.status_code == 200, "Upload failed"
        print(res.json())
        assert res.json()["fileName"] == "Test1", "Wrong file name"

    def test_upload_multiple_files(self):
        with open(self.File1, "rb") as f1, open(self.File2, "rb") as f2:
            files = {("files", f1), ("files", f2)}
            res = requests.post(f"{self.BASE_URL}/uploadMultipleFiles", files=files)
        print(res.json())
        assert res.status_code == 200, "Upload failed"
        print(res.json())
        #assert file names
        data = res.json()
        assert data[0]["fileName"] == "Test1", "Wrong file name"
        assert data[1]["fileName"] == "Test2", "Wrong file name"

    def test_download_file(self):
        filename = "Test1"
        res = requests.get(f"{self.BASE_URL}/downloadFile/{filename}")
        assert res.status_code == 200, "Download failed"
        output_path = f"downloaded_{filename}"
        with open(output_path, "wb") as file:
            file.write(res.content)
