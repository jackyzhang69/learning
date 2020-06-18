

function getNocSalary(noc,area_index) {



    // 去到页面，
    url='https://www.jobbank.gc.ca/trend-analysis/search-wages';

    // 差这一步： 如何去到页面？ 需要配置node.js的运行环境
    window.open(url)

    // 输入noc
    document.getElementById("ec-wages:wagesInput").value=noc;

    // pick one item from dropdown list: 还差这一步，如果选择drop list

    // click the search 目前到达这一步后，后面验证是正确的了。
    document.getElementById("searchWagesOccupationSubmit").click();


    // get salary data   
    // get all tr rows start with th 
    var area=document.querySelectorAll("tr th");
    // there is 86 rows with index starts from 5 （Canada), ends at 90 (Nunavut)
    // refer to area_index.xlsx
    var the_area=area[area_index];
    // the first sibling is lowest wage, the second is median, and the third is highest
    lowest=the_area.nextElementSibling.innerText;
    median=the_area.nextElementSibling.nextElementSibling.innerText;
    highest=the_area.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
    // above codes were tested correctly.
    
}

getNocSalary('0014',5)

