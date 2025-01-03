/* 시간에 관련한 변수  0.01(10ms)초 단위로 증가*/
const TimeVar = document.querySelector(".current-time");
let elapsedTime = 0;

/* 타임 포매팅한 문자열 반환하는 함수수 */
function Timeformating(ms){
    const Second = Math.floor((ms / 1000) % 60 );
    const mSecond = Math.floor((ms / 10) % 100);

    return `${String(Second).padStart(2,"0")}:${String(mSecond).padStart(2,"0")}`
}

/* ssr부분 버튼들 가져오기 */
const Buttons = document.querySelectorAll(".ssrButtons")
const startButton = Buttons[0]
const stopButton = Buttons[1]
const resetButton = Buttons[2]

/* 레코드 기록에 필요한 객체들 가져오기 */
const recordsContainer = document.querySelector(".records-container");

/* 작동 상태 변수 */
let intervalID = 0; // 0일때 멈춰있는다!

/* 헤더 스타트, 스톱, 리셋 버튼 기능 구현 */
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
    appendRecordsContainer(); // 뒤에 구현
}

function resetButtonClick(){
    if(intervalID == 0){ // reset은 스톱워치가 멈춰있을때만 작동한다!
        elapsedTime = 0;
        TimeVar.textContent = Timeformating(elapsedTime);
    }
}

/* 스톱 버튼 레코드 관련 기능 구현 */
function appendRecordsContainer(){
    const recordsContent = document.createElement("div");
    const childDiv1 = document.createElement("div");
    const childDiv2 = document.createElement("div");

    recordsContent.className = "records-content";
    childDiv2.className = "transparent-item"

    childDiv1.textContent = `${Timeformating(elapsedTime)}`;

    recordsContent.innerHTML = `
                    <div class="content__svg-slc-container">
                        <svg class="unSelectedButton" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
                        </svg>
                        <svg class="SelectedButton" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
                            <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"></path>
                        </svg>
                    </div>
                    `;
    recordsContent.appendChild(childDiv1);
    recordsContent.appendChild(childDiv2);

    /*선택 버튼 기능추가 */
    const svgButtons = recordsContent.querySelectorAll("svg");
    const unSelectedButton = svgButtons[0];
    const SelectedButton = svgButtons[1];   

    unSelectedButton.addEventListener("click",()=>{
        unSelectedButton.style.display = "none";
        SelectedButton.style.display = "block";
    })
    SelectedButton.addEventListener("click",()=>{
        SelectedButton.style.display = "none";
        unSelectedButton.style.display = "block";
    })

    recordsContainer.appendChild(recordsContent);
}
/* s,s,r 기능 구현 main */
startButton.addEventListener("click" , (event)=>{startButtonClick()})
stopButton.addEventListener("click" , ()=>{stopButtonClick()})
resetButton.addEventListener("click" , ()=>{resetButtonClick()})
/* ----------------------------------------------------------------------- */

/* 전체선택 기능 구현    */
const AllheaderButtons = document.querySelector(".header-svg-button");
const AllSelectButton = AllheaderButtons.querySelector(".SelectedButton");
const AllUnSelectButton = AllheaderButtons.querySelector(".unSelectedButton");

AllUnSelectButton.addEventListener("click",()=>{
    AllUnSelectButton.style.display = "none";
    AllSelectButton.style.display = "block";

    /* 모두 체크 하는 기능 */
    const allContainer = document.querySelectorAll(".content__svg-slc-container");

    allContainer.forEach((container)=>{
        const svgUnselec = container.querySelector(".unSelectedButton");
        const svgSelec = container.querySelector(".SelectedButton");

        if(getComputedStyle(svgUnselec).display == "block"){
            svgUnselec.style.display = "none";
            svgSelec.style.display = "block";
        }
    })
})
AllSelectButton.addEventListener("click",()=>{
    AllSelectButton.style.display = "none";
    AllUnSelectButton.style.display = "block";

    /* 모두 체크 하는 기능 */
    const allContainer = document.querySelectorAll(".content__svg-slc-container");

    allContainer.forEach((container)=>{
        const svgUnselec = container.querySelector(".unSelectedButton");
        const svgSelec = container.querySelector(".SelectedButton");

        if(getComputedStyle(svgSelec).display == "block"){
            svgSelec.style.display = "none";
            svgUnselec.style.display = "block";
        }
    })
})

/* 클리어 기능 구현 */
const clearButton = document.getElementById("ClearButton");

clearButton.addEventListener("click" ,()=>{
    const records = document.querySelectorAll(".records-content");

    records.forEach(record=>{
        const selectedButton = record.querySelector(".SelectedButton");
        if(selectedButton && selectedButton.style.display == "block"){
            record.remove();
        }
    })
    const AllheaderButtons = document.querySelector(".header-svg-button");
    const AllSelectButton = AllheaderButtons.querySelector(".SelectedButton");
    const AllUnSelectButton = AllheaderButtons.querySelector(".unSelectedButton");
    AllSelectButton.style.display = "none";
    AllUnSelectButton.style.display = "block";

})
/* ------------------------- */
