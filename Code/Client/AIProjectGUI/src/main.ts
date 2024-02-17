import {createRow} from "./row.ts"


let inputText = document.getElementById("input-text") as HTMLTextAreaElement
let button = document.getElementById("classify-button") as HTMLButtonElement
let results = document.getElementById("results") as HTMLDivElement
//let outputText = document.getElementById("output-text") as HTMLTextAreaElement



let data: JSON


button.onclick = async () => {

    let input = inputText.value

    results.innerHTML = ""

    inputText.classList.add("color-red")
    

    let link = "http://localhost:8080/predict"+"?text="+input

    console.log(link)
    let response = await fetch(link, {
        method: "POST"
    })

 
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body
        inputText.classList.remove("color-red")
        data = await response.json();
        console.log(data);
        //outputText.value = JSON.stringify(data);
    } else {
        console.error("HTTP-Error: " + response.status);
    }


    let map = new Map<number, number>(
        Object.entries(data).map(([key, value]) => [parseInt(key), parseFloat(value)])
        );

    let sortedMap = new Map<number, number>(
        Array.from(map.entries()).sort((a, b) => b[1] - a[1])
        );
    
    console.log(sortedMap)

    for (let [key, value] of sortedMap.entries()) {
        createRow(key, value)
    }




}




