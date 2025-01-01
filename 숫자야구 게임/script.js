// 기본적인 변수들 만들기
const maxAttempts = 9;
let attempts = maxAttempts;
const inputcollection = document.querySelector('.input-box');
const inputArray = Array.from(inputcollection.children);
    //남은 횟수 표현
const remainAttempts = document.querySelector('#attempts');
remainAttempts.innerText = `${attempts}`; 

// 정답 만들기
const getRandomInt = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};
function getAnswerArray(){
    const arr =new Set();
    while(arr.size < 3){
        const randnum = getRandomInt(1,9);
        arr.add(randnum);
    }
    return Array.from(arr);
}
const AnswerArray = getAnswerArray();

// ArrayCompare : 답과 입력을 비교할때 사용
function ArrayCompare(arr1 , arr2){
    return arr1.every((value,index) => value == arr2[index]);
}

//마지막 숫자에서 엔터 누르면 클릭이벤트 구현
inputArray[2].addEventListener("keypress" , event => {
    if(event.code == "Enter"){
        check_numbers();
    }
})

//스트라이크, 볼, 아웃 개수 세기기
function strike(values , AnswerArray){
    let res = 0;
    for(let i = 0; i < 3; i++){
        if(values[i] == AnswerArray[i]){
            res++;
        }
    }
    return res;
}
function ball(values , AnswerArray){
    let res = 0;
    for(let i = 0; i < 3; i++){
        for(let j = 0; j < 3 ; j++){
            if(i == j) continue;
            else if(values[i] == AnswerArray[j]){
                res++;
            }
        }
    }
    return res;
}
function out(values , AnswerArray){
    let res = 0;
    for(let i = 0; i < 3; i++){
        for(let j = 0; j < 3 ; j++){
            if(values[i] == AnswerArray[j]){
                res++;
            }
        }
    }
    return (res==0 ? 1 : 0);
}

// 삽입할 HTML스트링 만들기기
function createHTMLstring(values,AnswerArray){
    if(out(values,AnswerArray)){
        return `
        <div class="check-result left">
            <div>${values[0]} ${values[1]} ${values[2]}</div>
            <div>:</div>
            <div>
                <div class="num-result out">O</div>
            </div>
    `}
    else{
        return `
            <div class="check-result left">
                <div>${values[0]} ${values[1]} ${values[2]}</div>
                <div>:</div>
                <div>
                    ${strike(values,AnswerArray)}
                    <div class="num-result strike">S</div>
                    ${ball(values,AnswerArray)}
                    <div class = "num-result ball">B</div>
                </div>
        `
    }
}


//기록 디스플레이에 띄우기
function displayRecord(values){
    const displayResult = document.querySelector('.result-display');
    displayResult.insertAdjacentHTML("beforeend" ,createHTMLstring(values,AnswerArray));

}

//성공 실패시 디스플레이에 이미지 띄우기기
function displayImg(route){
    const gameResult = document.querySelector('.game-result');
    gameResult.innerHTML = `<img src = ${route} id ="game-result-img">`;
}

/* 
//tests----------------------------------------------------
console.log(AnswerArray);
//---------------------------------------------------------
*/

EndGame = 0 ;

// 확인하기 버튼 눌렀을때 구현
function check_numbers(){
    if(!EndGame){
        // 1. 값이 3개 다 차있지 않으면 alert발생 시킨뒤 입력창 비움
        const allValuesNotFilled = Array.from(inputcollection.children).some(input => input.value.trim() === "");
        
        if(allValuesNotFilled) {
            inputArray.forEach(input => {input.value = ""});
            alert("3글자를 다 입력하지 못하였습니다.");
            return;
        }

        // 1.5 입력값값 어레이 생성
        const values = Array.from(inputArray).map(input => Number(input.value));

        // 2. 디스플레이에 기록 띄우기
        displayRecord(values);

        // 3. 같으면 성공 다르면 실패
        if(ArrayCompare(values , AnswerArray)){
            displayImg("./success.png");
            EndGame= 1;
        }
        else{
            if(attempts == 0){
                displayImg("./fail.png");
                EndGame =1;
            }
        }
        // 4. 시도 후에 시도횟수 변경
        if(attempts >0){
        attempts--;
        remainAttempts.innerText = `${attempts}`; 
        }

        // 5. 시도 후에 입력창 초기화
        inputArray[0].value ="";
        inputArray[1].value ="";
        inputArray[2].value ="";

    }
    else{
        return;
    }

}