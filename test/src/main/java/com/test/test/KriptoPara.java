package com.test.test;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;


@Entity
public class KriptoPara {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String adi;
    private Double sonDeger;
    private Double degisimYuzde;
    private String tarih;
	public String getAdi() {
		return adi;
	}
	public void setAdi(String adi) {
		this.adi = adi;
	}
	public Double getSonDeger() {
		return sonDeger;
	}
	public void setSonDeger(Double sonDeger) {
		this.sonDeger = sonDeger;
	}
	public Double getDegisimYuzde() {
		return degisimYuzde;
	}
	public void setDegisimYuzde(Double degisimYuzde) {
		this.degisimYuzde = degisimYuzde;
	}
	public String getTarih() {
		return tarih;
	}
	public void setTarih(String tarih) {
		this.tarih = tarih;
	}
    
    // getters and setters
}
