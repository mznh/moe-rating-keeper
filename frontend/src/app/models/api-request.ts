import {PlayerData,BattleData} from './data';

export interface RegisterCharactorResult{
  status: string;
  player: PlayerData;
};


export interface ResultOfRecordBattle{
  status: string;
}
export interface RequestOfRecordBattle{
  side_a_name: string;
  side_a_token: string;
  side_b_name: string;
  side_b_token: string;
  winner_token: string;
}

export interface ResultOfFetchBattle{
  battles:BattleData[];

}
