//-------------------------------------------------------------------------------------------------
//
// File name   : div2.sv
// Author      : Arhum Alam
//
//-------------------------------------------------------------------------------------------------
//
// The objective is to design an implementation that meets the following specification:
// A synchronous divide-by-2 circuit for creating a slowed-down version of the input clock.
//
// Components available as options include:
// - D-Type Flop
// - Standard combinatorial cells (INV, NAND, NOR, XOR etc.)
// You may want so draw the circuit diagram for this, and/or write down the HDL description
// (Verilog or VHDL).
//
// Waveform:
// Consider what the output of the circuit should look like to meet the specification i.e. complete
// the "O/p" waveform in the following waveform diagram (i.e. complete a few cycles of the waveform
// of the signal "O/p")
//
// Additional Question:
// What would be needed to add the feature of an input that enabled/disabled the output clock?
// (e.g. as a power-saving feature when that divided clock was not needed).
//
//-------------------------------------------------------------------------------------------------

module div2 (
    in_clk,
    reset,
    out_clk
);
    input logic in_clk;
    input logic reset;
    output logic out_clk;

    // Toggle the clock every time an "in_clk" posedge is seen.
    // This means there would have to be two "in_clk" posedges seen to cover one period of out_clk.
    always_ff @ (posedge in_clk) begin
        if (reset) begin
            out_clk <= 1'b0;
        end
        else begin
            out_clk <= ~out_clk;
        end
    end

endmodule