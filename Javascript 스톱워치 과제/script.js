/* 시간에 관련한 변수  0.01(10ms)초 단위로 증가*/
const TimeVar = document.querySelector(".current-time");
let elapsedTime = 0;

function Timeformating(ms){
    const Second = Math.floor((ms / 1000) % 60 );
    const mSecond = Math.floor((ms / 10) % 100);

    return `${String(Second).padStart(2,"0")}:${String(mSecond).padStart(2,"0")}`
}


/* 헤더부분 클릭이벤트 구현 */
const Buttons = document.querySelectorAll(".ssrButtons")
const startButton = Buttons[0]
const stopButton = Buttons[1]
const resetButton = Buttons[2]


/* 작동 상태 변수 */
let intervalID = 0; // 0일때 멈춰있는다!


function startButtonClick(){
    if(!intervalID){
        intervalID = setInterval(()=>{
            elapsedTime += 10
            TimeVar.textContent = Timeformating(elapsedTime);
        },10)
    }
}
function stopButtonClick(){
    clearInterval(intervalID);
    intervalID = 0;
}

startButton.addEventListener("click" , (event)=>{startButtonClick()})
stopButton.addEventListener("click" , ()=>{stopButtonClick()})
resetButton.addEventListener("click" , ()=>{


})


/* tests */
