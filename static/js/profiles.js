
    function update() {
        var update = document.getElementById("update");
        var show_profile = document.getElementById("show_profile");
        var save_form = document.getElementById("save_form");
        update.style.display = "none";
        show_profile.style.display = "none";
        save_form.style.display = "block";
    }
    var hidden_field = document.getElementById("hidden").value;
    if (hidden != "") {
        show_profile.style.display = "block";
        save_form.style.display = "none";
    


    }
    // ---setting up to connect with Firebase-------------------------------------------------------
    var ImgName, ImgUrl;
    var files = [];
    var reader
    var config = {
        // use your key credentials as I have removed them from below
        apiKey: "your api key",
        authDomain: "krishworks-104a4.firebaseapp.com",
        databaseURL: "https://krishworks-104a4-default-rtdb.firebaseio.com",
        projectId: "krishworks-104a4",
        storageBucket: "krishworks-104a4.appspot.com",
        messagingSenderId: "your key",
        appId: "1:your app id",
        measurementId: "your id"
    };
    firebase.initializeApp(config);
    // creating  element of type file on clicking on the element
    document.getElementById("select").onclick = function () {
        var input = document.createElement("input");
        input.type = "file";
        input.setAttribute("accept", "image/png, image/gif, image/jpeg ,image/jpg")
        input.onchange = e => {
            var extensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
            files = e.target.files;
            if (!extensions.exec(input.value)) {
                alert('File extension is invalid');
                input.value = '';
            }

        }
        input.click();
        setTimeout(function () { document.getElementById("upload").style.display = "block"; }, 2000)

    }
    // -----------------Image---Upload logic
    document.getElementById("upload").onclick = function () {
        ImgName = document.getElementById("namebox").value;
        const filename = Math.floor(Date.now() / 1000);
        // setting the name of image to be uploaded on Firebase db
        var uploadTask = firebase.storage().ref("Images/" + ImgName + filename + ".png").put(files[0]);
        uploadTask.on("state_changed", function (snapshot) {

            // image upload progress logic while uploading
            var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
            document.getElementById("upProgress").innerHTML = "Upload" + " " + progress + "%";
            if (progress == 100) {
                document.getElementById("upload").style.display = "none";
            }
        },
            // handling error
            function (error) {
                alert("error")
            },
            function () {
                uploadTask.snapshot.ref.getDownloadURL().then(function (url) {
                    ImgUrl = url;
                    document.getElementById("url").value = ImgUrl;

                    document.getElementById("postlink").click();

                    firebase.database().ref("Pictures/" + ImgName).set({
                        Name: ImgName,
                        Link: ImgUrl
                    })
                }
                )
            });
    }


