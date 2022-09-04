export interface SaveData{
  nowLoginKey: string;
  players: PlayerData[];
};


export function generateDefaultSaveData(){
  return {
    nowLoginKey: "",
    players: [ ]
  }
}
export interface PlayerData{
  key: string;
  token: string;
  name: string;
  server: string;
}

export function generateDefaultPlayerData(){
  return {
    key: "",
    token: "",
    name: "",
    server: ""
  }
}

export interface BattleData{
  side_a_name:string;
  side_b_name:string;
  winner_name:string
}

