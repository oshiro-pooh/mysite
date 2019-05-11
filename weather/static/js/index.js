// 初期化処理
(function () {
    addEvent();
    alert('読み込み成功');
}());

function addEvent(){
  //オブジェクト"id_prefs"のchangeイベントにshowMessage関数を追加する
  document.getElementById("id_prefs").addEventListener("change", changePrefs, false);
}
 
function changePrefs(){
  this.form.submit();
}