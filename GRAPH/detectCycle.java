package GRAPH;
import java.util.AbstractMap.SimpleEntry;

import javax.swing.plaf.TreeUI;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class detectCycle {

    public boolean checkForCycle(int src,int V, ArrayList<ArrayList<Integer>> adj, boolean[] vis){

        vis[src] = true;
        Queue<SimpleEntry<Integer, Integer>> q = new LinkedList<>();
        q.add(new SimpleEntry<>(src, -1));

        while(!q.isEmpty()){
            int node = q.peek().getKey();
            int parent = q.peek().getValue();
            q.remove();

            for(int adjnode: adj.get(node)){
                if(vis[adjnode] == false){
                    vis[adjnode] = true;
                    q.add(new SimpleEntry<>(adjnode,node));

                }else if(parent != adjnode){
                    return true;
                }
            }

        
        }
        return false;

    }
    public boolean isCycle(int V,ArrayList<ArrayList<Integer>> adj){

        boolean vis[] = new boolean[V];
        for (int i = 0; i < vis.length; i++) {
            vis[i] = false;
        }
        for (int i = 0; i < vis.length; i++) {
            if(vis[i] == false){
                if(checkForCycle(i, V, adj, vis)){
                    return true;
                }
            }
        }
        return false;
    }

    
}