module div2_tb;
    logic in_clk;
    logic reset;
    logic out_clk;

    initial begin
        in_clk = 1'b0;
        forever #5 in_clk = ~in_clk;
    end

    initial begin
        reset = 1'b1;
        #10 reset = 1'b0;
    end

    div2 div2_inst (.*);
endmodule