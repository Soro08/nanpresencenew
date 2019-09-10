var myChart = echarts.init(document.getElementById('main'), null, {renderer: 'svg'});
var myGausChart = echarts.init(document.getElementById('gaus'));
var note = [15, 20, 36, 90, 60, 20]
// specify chart configuration item and data
var mymoyenne = 30;
var option = {
    backgroundColor: '',
    title: {
        text: 'Résultat Quiz'
    },
    tooltip: {
        show: false
    },
    legend: {
        textStyle: {
            color: 'rgba(255, 255, 255, 0.3)'
        },
        data:['Notes'],
        
    },
    toolbox: {
        show : true,
        showTitle: true,
        feature : {
            //dataView : {show: true, readOnly: false},
            magicType : {
                show: true,
                title: 'view',
                type: ['line', 'bar']},
            //restore : {show: true},
            saveAsImage : {
                show: true,
                title: 'Save',
                },
            dataView: {
                show: true,
                title: 'Data View'
            },
        }
    },
    calculable : true,
    xAxis: {
        data: ["kkd","dddd","fff shirt","ffff","ffff","socks"],
        
    },
    
    yAxis: {},
    series: [{
        name: 'Notes',
        type: 'bar',
        itemStyle: {
            // Styles for normal state.
            normal: {
                color: '#661058'
            },
            // Styles for emphasis state.
            emphasis: {
                color: '#981883'
            }
        },
        data: note.sort(function(a, b){return a-b}).reverse(),
        markLine : {
            data : [
                {type : 'average', name: 'Moyenne'}
            ]
        }
    }]
};

// use configuration item and data specified to show chart
myChart.setOption(option);

// Gauss options

gauge_option = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    
    series: [
        {
            name: 'Note',
            type: 'gauge',
            detail: {formatter:'{value}%'},
            data: [{value: 50, name: 'Soro'}]
        }
    ]
};

setInterval(function () {
    gauge_option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
    myGausChart.setOption(gauge_option, true);
},2000);

//myGausChart.setOption(gauge_option);