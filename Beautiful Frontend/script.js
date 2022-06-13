function updateTextInput(val) {
          document.getElementById('SalaryInput').value = val; 
}
function updateTextInput2(val) {
          document.getElementById('SalaryInput2').value = val; 
}

let cities = ['Гусь-Хрустальный', 'Ишимбай', 'Юрга', 'Томск', 'Октябрьский',
       'Нижний Новгород', 'Калтан', 'Туапсе', 'Уфа', 'Санкт-Петербург',
       'Туймазы', 'Прокопьевск', 'Нефтекамск', 'Анапа', 'Тюмень',
       'Кропоткин', 'Белебей', 'Мелеуз', 'Стерлитамак', 'Белорецк',
       'Армавир', 'Сергиев Посад', 'Воронеж', 'Ставрополь', 'Ярославль',
       'Краснодар', 'Челябинск', 'Брянск', 'Бураево', 'Омск',
       'Ростов-на-Дону', 'Москва', 'Бирск', 'Салават', 'Сибай',
       'Старый Оскол', 'Набережные Челны', 'Давлеканово', 'Мраково',
       'Екатеринбург', 'Новосибирск', 'Пермь', 'Смоленск', 'Янаул',
       'Дюртюли', 'Боровичи', 'Киселёвск', 'Учалы', 'Белгород',
       'Магнитогорск', 'Ижевск', 'Чусовой', 'Вологда', 'Ейск', 'Тверь',
       'Верхние Татышлы', 'Кунгур', 'Сочи', 'Раменское', 'Осинники',
       'Кумертау', 'Таганрог', 'Иглино', 'Тула', 'Тамбов',
       'Новокузнецк', 'Одинцово', 'Месягутово', 'Светлый', 'Киргиз-Мияки',
       'Каневская', 'Орёл', 'Владимир', 'Языково', 'Сургут', 'Муром',
       'Кореновск', 'Вольск', 'Красноярск', 'Великий Новгород',
       'Кемерово', 'Иркутск', 'Верхнеяркеево', 'Дзержинск', 'Пенза',
       'Глазов', 'Нижневартовск', 'Ковров', 'Баймак', 'Чишмы',
       'Новороссийск', 'Аскино', 'Мегион', 'Рязань', 'Саратов', 'Покров',
       'Стерлибашево', 'Зилаир', 'Жуковский', 'Златоуст', 'Белово',
       'Благовещенск', 'Череповец', 'Толбазы', 'Раевский', 'Калтасы',
       'Сарапул', 'Самара', 'Архангельск', 'Старосубхангулово',
       'Пятигорск', 'Аскарово', 'Геленджик', 'Федоровка',
       'Старобалтачево', 'Миасс', 'Воскресенск', 'Волгоград', 'Серпухов',
       'Бийск', 'Невинномысск', 'Клинцы', 'Серафимовский', 'Барнаул',
       'Ульяновск', 'Калининград', 'Рославль', 'Воткинск', 'Тимашевск',
       'Красноусольский', 'Химки', 'Междуреченск', 'Надым', 'Караидель',
       'Курган', 'Липецк', 'Архангельское', 'Петрозаводск', 'Исянгулово',
       'Курганинск', 'Казань', 'Приютово', 'Колпино', 'Кандры', 'Дубна',
       'Агидель', 'Березники', 'Янгантау', 'Ангарск', 'Николо-Березовка']


function extendDatalist() {
    for (let i = 0; i < cities.length; i++) {
        let element = document.createElement('option');
        element.value = cities[i];
        document.getElementById('cities-datalist').append(element);
    }
}
extendDatalist();



function insertResult() {
    for (let i = 1; i <= 32; i++) {
        document.querySelector('table tbody tr:nth-child(' + i + ') th').append("Privet");
    }
}

// insertResult();

let calculated = false;

function spawnTable() {
    if (calculated == true) return;
    calculated = true;
    let table = document.createElement('table');
    // ctx.classList.add("firstChart");
    table.append('thead');


    document.querySelector('.placeForTable').append(table);
}






function spawnChart() {
    if (calculated == true) return;
    calculated = true;
    let ctx = document.createElement('canvas');
    ctx.classList.add("firstChart");
    document.querySelector('.placeForCharts').append(ctx);

    let myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [0, 1, 2, 3, 4, 5],  // Значения по x
            datasets: [{
                label: 'Помидоры',
                data: [20, 50, 42, 28, 77, 22],
                backgroundColor: [
                    'white'
                ],
                borderColor: [
                    'red'
                ],
                borderWidth: 4
            },
            {
                label: 'Баклажаны',
                data: [7, 90, 21, 3, 24, 47],
                backgroundColor: [
                    'white'
                ],
                borderColor: [
                    'blue'
                ],
                borderWidth: 4
            },
            {
                label: 'Огурцы',
                data: [39, 33, 36, 29, 65, 88],
                backgroundColor: [
                    'white'
                ],
                borderColor: [
                    'green'
                ],
                borderWidth: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Отношение популярности баклажанов к помидорам'
              }
            }
        },
    })
}
// let ctx = document.querySelector('.firstGraph').getContext('2d');

// spawnChart();

