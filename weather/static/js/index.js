// 初期化処理
window.onload = function() {
    addEvent();
};

// イベント追加処理
function addEvent(){
    //オブジェクト"id_prefs"のchangeイベントにshowMessage関数を追加する
    document.getElementById("id_prefs").addEventListener("change", changePrefs, false);
}

// 都道府県名変更時イベント 
function changePrefs(){
  if(document.getElementById("id_prefs").value !== '') {
    // 都道府名プルダウンで空白以外を選んだ場合
    document.getElementById("searchWeather").click()
  } else {
    // 都道府名プルダウンで空白を選んだ場合
    // 市町村名プルダウンの選択値リストを削除
    var cities = document.getElementById("id_cities");
    while (cities.firstChild) cities.removeChild(cities.firstChild);
    
    // 市町村名プルダウンに空白を追加
    // option要素の宣言
    var option = document.createElement('option');
    // option要素のvalue属性に値をセット
    option.setAttribute('value', '');
    // option要素に値をセット
    option.innerHTML = '';
    // 作成したoption要素をselectタグに追加
    cities.appendChild(option);
  }
}