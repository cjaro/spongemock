const args = process.argv.slice(2);
const phraseToMock = args[0];

function spongeMock(str) {
    var arr = str.split("");
    var output = "";
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] !== " ") {
            var z = Math.floor(Math.random() * 2);
            if (z === 0) {
                output += arr[i].toLowerCase();
            } else {
                output += arr[i].toUpperCase();
            }
        } else {
            output += arr[i]
        }
    }
    console.log(output);
}
spongeMock(phraseToMock);